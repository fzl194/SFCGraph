---
id: UDG@20.15.2@MMLCommand@LST NGBINDUEMUTWL
type: MMLCommand
name: LST NGBINDUEMUTWL（查询5G LAN组绑定PA口UE互访白名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGBINDUEMUTWL
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN用户互访控制
- UE互访白名单绑定5G LAN组
status: active
---

# LST NGBINDUEMUTWL（查询5G LAN组绑定PA口UE互访白名单）

## 功能

**适用NF：UPF**

该命令用于查询5G LAN组下绑定的PA口UE互访白名单。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGBINDUEMUTWL]] · 5G LAN组绑定PA口UE互访白名单（NGBINDUEMUTWL）

## 使用实例

查询5G LAN组a0000001-460-01-01下绑定的PA口UE互访白名单：

```
LST NGBINDUEMUTWL: VNINSTANCE="a0000001-460-01-01";
```

```

RETCODE = 0  Operation succeeded

结果如下
------------------------
白名单名称

whilt1           
whilt2           
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NGBINDUEMUTWL.md`
