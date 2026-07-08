---
id: UDG@20.15.2@MMLCommand@CLR NGLANLEARNMAC
type: MMLCommand
name: CLR NGLANLEARNMAC（清除5G LAN学习的MAC地址）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: NGLANLEARNMAC
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN MAC地址维护
- 清除5G LAN学习的MAC地址
status: active
---

# CLR NGLANLEARNMAC（清除5G LAN学习的MAC地址）

## 功能

**适用NF：UPF**

该命令用于删除5G LAN组学习到的MAC地址。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VnInstance以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |
| MACADDR | MAC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度为17位。字符串应符合MAC地址格式，如fa-16-3e-49-07-ec。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGLANLEARNMAC]] · 5G LAN学习的MAC地址（NGLANLEARNMAC）

## 使用实例

删除学习到的5G LAN组"A0000001-460-003-01"的MAC地址“aa-bb-cc-dd-ee-ff”：

```
CLR NGLANLEARNMAC: VNINSTANCE="A0000001-460-003-01", MACADDR="aa-bb-cc-dd-ee-ff";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/CLR-NGLANLEARNMAC.md`
