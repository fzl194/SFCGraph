---
id: UDG@20.15.2@MMLCommand@LST NETWORKINSTVPNMAP
type: MMLCommand
name: LST NETWORKINSTVPNMAP（查询网络实例配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NETWORKINSTVPNMAP
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 网络实例管理
- 网络实例配置
status: active
---

# LST NETWORKINSTVPNMAP（查询网络实例配置）

## 功能

**适用NF：UPF**

该命令用来查看指定网络实例或者已配置所有的网络实例的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETWORKINSTANCE | 网络实例名称 | 可选必选说明：可选参数<br>参数含义：网络实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～100，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [网络实例配置（NETWORKINSTVPNMAP）](configobject/UDG/20.15.2/NETWORKINSTVPNMAP.md)

## 使用实例

显示指定网络实例"net1"的信息：

```
%%LST NETWORKINSTVPNMAP: NETWORKINSTANCE="net1";
```

```
%%
RETCODE = 0 操作成功

网络实例信息
----------------------------
  网络实例名称 = net1
       绑定VPN = ENABLE
     VPN实例名 = VPN2auto
  绑定IPv6 VPN = DISABLE
IPv6 VPN实例名 = NULL
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网络实例配置（LST-NETWORKINSTVPNMAP）_91144212.md`
