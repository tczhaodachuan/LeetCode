import time

import numpy as np
import pyarrow as pa
import pyarrow.plasma as plasma

client = plasma.connect("/tmp/plasma")

data = np.random.randn(100000000)
tensor = pa.Tensor.from_numpy(data)

object_id = plasma.ObjectID(np.random.bytes(20))
buf = client.create(object_id, pa.get_tensor_size(tensor))

stream = pa.FixedSizeBufferWriter(buf)
stream.set_memcopy_threads(4)
a = time.time()
pa.write_tensor(tensor, stream)
print("Writing took ", time.time() - a)
