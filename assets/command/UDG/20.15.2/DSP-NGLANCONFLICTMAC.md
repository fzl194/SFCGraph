---
id: UDG@20.15.2@MMLCommand@DSP NGLANCONFLICTMAC
type: MMLCommand
name: DSP NGLANCONFLICTMAC（显示5G LAN冲突MAC地址信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NGLANCONFLICTMAC
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN MAC地址维护
- 显示5G LAN冲突MAC地址信息
status: active
---

# DSP NGLANCONFLICTMAC（显示5G LAN冲突MAC地址信息）

## 功能

**适用NF：UPF**

该命令用于显示5G LAN组冲突的MAC地址信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VnInstance以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGLANCONFLICTMAC]] · 5G LAN冲突MAC地址信息（NGLANCONFLICTMAC）

## 使用实例

查询组名称为a0000001-460-003-01的5G LAN组的冲突MAC地址信息：

```
%%DSP NGLANCONFLICTMAC: VNINSTANCE="a0000001-460-003-01";
```

```
%%
RETCODE = 0  操作成功

5G LAN冲突MAC地址信息
---------------------
Result  =  
                      Mac Address  =  F0-F2-F3-F4-F5-F6
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示5G-LAN冲突MAC地址信息（DSP-NGLANCONFLICTMAC）_71960169.md`
