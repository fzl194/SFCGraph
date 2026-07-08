---
id: UNC@20.15.2@MMLCommand@RMV NGUSRGRPMEM
type: MMLCommand
name: RMV NGUSRGRPMEM（删除5G用户群成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGUSRGRPMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 用户群组成员管理
status: active
---

# RMV NGUSRGRPMEM（删除5G用户群成员）

## 功能

![](删除5G用户群成员（RMV NGUSRGRPMEM）_44007670.assets/notice_3.0-zh-cn_2.png)

执行该命令，当仅输入USRGRPID时将删除所有5G用户群成员。

**适用NF：AMF**

该命令用于删除5G用户群成员。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGUSRGRPMEM]] · 5G用户群成员（NGUSRGRPMEM）

## 使用实例

删除用户群成员记录，用户群标识为20，执行如下命令：

```
RMV NGUSRGRPMEM: USRGRPID=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGUSRGRPMEM.md`
