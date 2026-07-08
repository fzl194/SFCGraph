---
id: UDG@20.15.2@MMLCommand@DSP LDPNEMGADJ
type: MMLCommand
name: DSP LDPNEMGADJ（显示LDP的邻居信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPNEMGADJ
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

# DSP LDPNEMGADJ（显示LDP的邻居信息）

## 功能

该命令用于显示LDP的邻居信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示LDP邻居的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示LDP对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LDPNEMGADJ]] · LDP的邻居信息（LDPNEMGADJ）

## 使用实例

显示LDP的邻居信息：

```
DSP LDPNEMGADJ:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
             VPN实例名称  =  _public_
          对等体的LSR ID  =  10.10.10.10
                实体编号  =  1
                    状态  =  LDP邻居处于稳态
                    类型  =  本地邻居
                  源地址  =  192.168.3.3
              接口索引值  =  10
                接口名称  =  Ethernet66/0/7
                传输地址  =  10.10.10.10
对等体Hello保持时间（s）  =  15
  本端Hello保持时间（s）  =  15
              备份版本号  =  30
              平滑版本号  =  1
                调度状态  =  完成发布或未发布
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LDPNEMGADJ.md`
