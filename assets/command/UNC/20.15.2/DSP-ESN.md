---
id: UNC@20.15.2@MMLCommand@DSP ESN
type: MMLCommand
name: DSP ESN（查询ESN）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ESN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP ESN（查询ESN）

## 功能

该命令用于查询设备ESN。

## 注意事项

无

## 参数

无。

## 操作的配置对象

- [设备序列号（ESN）](configobject/UNC/20.15.2/ESN.md)

## 使用实例

查询设备ESN：

```
%%DSP ESN:;%%
RETCODE = 0  操作成功

设备序列号
----------
设备序列号  =  0123456789
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ESN(DSP-ESN)_00221880.md`
