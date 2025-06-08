# MicroPython Timezone Lookup

A compact, pre-generated MicroPython-compatible timezone lookup library based on the [Nayarsystems POSIX TZ database](https://github.com/nayarsystems/posix_tz_db).

## 📦 Files

- `tz_data.py`: Precompiled timezone lookup table (`iana → posix`)
- `example.py`: How to use it

## 🛠 Usage

1. Upload both `tz_data.py` and `example.py` to your MicroPython board.
2. Run `example.py`.

```python
import tz_data
print(tz_data.lookup("America/New_York"))  # Example output: EST5EDT,M3.2.0,M11.1.0
```
