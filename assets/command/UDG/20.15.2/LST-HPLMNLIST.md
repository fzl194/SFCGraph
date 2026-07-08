---
id: UDG@20.15.2@MMLCommand@LST HPLMNLIST
type: MMLCommand
name: LST HPLMNLIST（查看UPF设备的归属PLMN）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HPLMNLIST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- 归属地PLMN
status: active
---

# LST HPLMNLIST（查看UPF设备的归属PLMN）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看UPF设备的归属PLMN。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/HPLMNLIST]] · UPF设备的归属PLMN（HPLMNLIST）

## 使用实例

查询UPF上归属PLMN：

```
LST HPLMNLIST:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
移动国家码  =  470
移动网络号  =  03
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HPLMNLIST.md`
