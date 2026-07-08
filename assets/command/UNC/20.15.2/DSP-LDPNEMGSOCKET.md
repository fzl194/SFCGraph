---
id: UNC@20.15.2@MMLCommand@DSP LDPNEMGSOCKET
type: MMLCommand
name: DSP LDPNEMGSOCKET（显示LDP邻居管理的Socket信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPNEMGSOCKET
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

# DSP LDPNEMGSOCKET（显示LDP邻居管理的Socket信息）

## 功能

该命令用于显示LDP邻居管理的Socket信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPNEMGSOCKET]] · LDP邻居管理的Socket信息（LDPNEMGSOCKET）

## 使用实例

显示LDP邻居管理的Socket信息：

```
DSP LDPNEMGSOCKET: VRFNAME="_public_";
```

```

RETCODE = 0  操作成功

结果如下
------------------------
VPN实例名称    LDP分配给Socket的编号    Socket分配给LDP的编号    UDP Socket的类型    LDP发送协议消息时使用的管道编号    LDP接收协议消息时使用的管道编号    UDP Socket被引用的次数      TCP Socket创建的状态    Socket的备份状态    LDP与Socket之间发生流控的标识    LDP与Socket之间发生流控的次数    Socket的备份类型    Socket备份版本号    拒绝UDP报文的数量统计     最后一次丢弃标识    最后拒绝UDP报文的时间
_public_       21                       1                        IPv4的多播Socket    524342                             1074266165                         2                           Socket创建成功          空闲状态            LDP与Socket之间未发生流控        41891                            备份类型无效        1                   0                         0                   NULL
_public_       22                       2                        IPv4的单播Socket    524344                             1074266167                         0                           Socket创建成功          空闲状态            LDP与Socket之间未发生流控        41891                            备份类型无效        1                   0                         0                   NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPNEMGSOCKET.md`
