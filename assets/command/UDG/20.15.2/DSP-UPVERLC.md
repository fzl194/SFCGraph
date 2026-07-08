---
id: UDG@20.15.2@MMLCommand@DSP UPVERLC
type: MMLCommand
name: DSP UPVERLC（显示设备EOS时间）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPVERLC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 设备管理
- 生命周期管理
status: active
---

# DSP UPVERLC（显示设备EOS时间）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

显示设备EOS时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [设备EOS时间（UPVERLC）](configobject/UDG/20.15.2/UPVERLC.md)

## 使用实例

当需要查询生命周期EOSTIME时，进行如下设置：

```
DSP UPVERLC:;
```

```

RETCODE = 0操作成功
 
结果如下
------------------------
设备EOS时间= 2028-12-31
（结果个数=1）
 
---结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示设备EOS时间（DSP-UPVERLC）_14363516.md`
