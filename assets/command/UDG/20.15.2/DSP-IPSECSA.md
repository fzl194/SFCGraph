---
id: UDG@20.15.2@MMLCommand@DSP IPSECSA
type: MMLCommand
name: DSP IPSECSA（显示IPsec安全联盟）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPSECSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec安全联盟
status: active
---

# DSP IPSECSA（显示IPsec安全联盟）

## 功能

该命令用于显示IPsec安全联盟。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SANAME | 安全联盟名称 | 可选必选说明：可选参数<br>参数含义：安全联盟名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |

## 操作的配置对象

- [IPsec安全联盟（IPSECSA）](configobject/UDG/20.15.2/IPSECSA.md)

## 使用实例

显示IPsec安全联盟：

```
DSP IPSECSA: SANAME="1";
```

```

RETCODE = 0  操作成功。

结果如下
--------
  安全联盟名称  =  1
SA配置是否完整  =  TRUE
      引用次数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IPsec安全联盟（DSP-IPSECSA）_50280750.md`
