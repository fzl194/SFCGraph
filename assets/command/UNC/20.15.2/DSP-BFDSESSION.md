---
id: UNC@20.15.2@MMLCommand@DSP BFDSESSION
type: MMLCommand
name: DSP BFDSESSION（查询BFD的会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BFDSESSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD会话
status: active
---

# DSP BFDSESSION（查询BFD的会话信息）

## 功能

该命令用于显示BFD会话的状态信息，可以按照本地描述符和目的地址过滤。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALDISCR | 本地标识符 | 可选必选说明：可选参数<br>参数含义：会话本地描述符。用于唯一标识本端会话。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～49152。<br>默认值：无 |
| DESTADDR | 目的IP地址 | 可选必选说明：可选参数<br>参数含义：会话检测链路的目的地址。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～128。IPv4或者IPv6地址。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BFDSESSION]] · BFD会话参数（BFDSESSION）

## 使用实例

显示目的地址为10.1.1.1的所有BFD会话的详细信息：

```
DSP BFDSESSION:DESTADDR="10.1.1.1";
```

```

RETCODE = 0  操作成功

结果如下
----------------
                  本地标识符  =  222
                  目的IP地址  =  10.1.1.1
                  远端标识符  =  222
                    源IP地址  =  10.1.1.2
                    检测倍数  =  3
          最小发送间隔（ms）  =  1000
          最小接收间隔（ms）  =  1000
单臂Echo会话的收包间隔（ms）  =  NULL
                    会话名称  =  Huawei123
                    会话状态  =  DOWN
                    会话类型  =  单跳IP会话
                  出接口名称  =  Ethernet64/0/3
                  报文优先级  =  7
          实际发送间隔（ms）  =  9689
          实际接收间隔（ms）  =  9689
              检测时间（ms）  =  0
                实际检测倍数  =  0
                  本地诊断字  =  无
                 VPN实例名称  =  NULL
               UDP目的端口号  =  3784
                会话绑定应用  =  No Application Bind
                    描述信息  =  NULL
                      RU名称  =  VNODE_VNRS_VNFC_IPU_0064
                 是否配置PST  =  FALSE
                 是否操作PST  =  FALSE
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BFDSESSION.md`
