---
id: UDG@20.15.2@MMLCommand@LST BFDSESSION
type: MMLCommand
name: LST BFDSESSION（查询BFD会话的配置信息）
nf: UDG
version: 20.15.2
verb: LST
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

# LST BFDSESSION（查询BFD会话的配置信息）

## 功能

该命令用于查询BFD会话配置信息，可以通过本地标识符过滤。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSNAME | 会话名称 | 可选必选说明：可选参数<br>参数含义：会话名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。不区分大小写，不支持空格。<br>默认值：无 |
| LOCALDISCR | 本地标识符 | 可选必选说明：可选参数<br>参数含义：会话本地描述符。用于唯一标识本端会话。BFD会话两端设备的本地标识符和远端标识符需要分别对应，即本端的本地标识符与对端的远端标识符相同，否则会话无法正确建立。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～16384。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BFDSESSION]] · BFD会话参数（BFDSESSION）

## 使用实例

查询所有的BFD会话配置：

```
LST BFDSESSION:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                    会话名称  =  Huawei123
                  本地标识符  =  1222
                  远端标识符  =  1234
          最小发送间隔（ms）  =  200
          最小接收间隔（ms）  =  200
                    检测倍数  =  3
         等待恢复时间（min）  =  NULL
                  报文优先级  =  7
                    管理DOWN  =  FALSE
                    描述信息  =  NULL
                IPv4目的地址  =  10.1.1.2
                  IPv4源地址  =  10.1.1.1
                会话链路类型  =  IP
                    创建方式  =  静态
                  出接口名称  =  Ethernet64/0/3
                 VPN实例名称  =  NULL
                    单臂Echo  =  不生效
单臂Echo会话的收包间隔（ms）  =  NULL
                IPv6目的地址  =  NULL
                  IPv6源地址  =  NULL
                 是否操作PST  =  FALSE

    (结果个数 = 1)
    ---  END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-BFDSESSION.md`
