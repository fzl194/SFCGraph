---
id: UDG@20.15.2@MMLCommand@CLR MMLCFGDOMAIN
type: MMLCommand
name: CLR MMLCFGDOMAIN（清除绑定域信息）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: MMLCFGDOMAIN
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 集中配置管理
- 公共命令配置域信息管理
status: active
---

# CLR MMLCFGDOMAIN（清除绑定域信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](清除绑定域信息（CLR MMLCFGDOMAIN）_55903167.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行本命令后将批量清除配置的域信息，且不可回退。

本命令用于批量清除配置中的域信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 公共配置命令名称 | 可选必选说明：必选参数<br>参数含义：公共配置命令名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [批量设置绑定域信息（MMLCFGDOMAIN）](configobject/UDG/20.15.2/MMLCFGDOMAIN.md)

## 使用实例

批量清除ADD APN命令所配置的域信息：

```
CLR MMLCFGDOMAIN: CMDNAME="ADD APN";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除绑定域信息（CLR-MMLCFGDOMAIN）_55903167.md`
