---
id: UNC@20.15.2@MMLCommand@DSP LDPLSPMGPEERADDR
type: MMLCommand
name: DSP LDPLSPMGPEERADDR（显示LDP的邻居地址信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPLSPMGPEERADDR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPLSPMGPEERADDR（显示LDP的邻居地址信息）

## 功能

该命令用于显示LDP的邻居地址信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| FECFLAG | 本地地址标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示LSP的本地地址标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PEER：指定对等体ID。<br>- ADDRESS：指定地址。<br>默认值：无 |
| ADDRESS | 本地地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“ADDRESS”时为必选参数。<br>参数含义：该参数用于表示LSP的本地地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PEERID | 对等体的LSR ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“FECFLAG”配置为“PEER”时为必选参数。<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [LDP的邻居地址信息（LDPLSPMGPEERADDR）](configobject/UNC/20.15.2/LDPLSPMGPEERADDR.md)

## 使用实例

显示LDP的邻居地址信息：

```
DSP LDPLSPMGPEERADDR:FECFLAG=ADDRESS,ADDRESS="10.1.1.2";
```

```

RETCODE = 0  操作成功。

结果如下
--------
   VPN实例名称  =  _public_
对等体的LSR ID  =  10.10.10.10
      本地地址  =  10.1.1.2
   通告FSM状态  =  已完成通告
 LDP备份版本号  =  0
 LDP平滑版本号  =  1
        组件ID  =  0x1c0037
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示LDP的邻居地址信息（DSP-LDPLSPMGPEERADDR）_49801738.md`
