---
id: UNC@20.15.2@MMLCommand@LST IFDSCP
type: MMLCommand
name: LST IFDSCP（查询接口DSCP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFDSCP
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- DSCP
- 接口DSCP管理
status: active
---

# LST IFDSCP（查询接口DSCP配置）

## 功能

**适用网元：SGSN、MME**

该命令用来查看 UNC 对外网元接口发送IP包时携带的DSCP值。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [接口DSCP配置（IFDSCP）](configobject/UNC/20.15.2/IFDSCP.md)

## 使用实例

查询 UNC 对外网元接口发送IP包时携带的DSCP配置：

LST IFDSCP:;

```
%%LST IFDSCP:;%%
RETCODE = 0  执行成功。

信令报文的DSCP查询结果如下
--------------
接口类型                     DSCP值
未指定接口                   56
S1_MME接口                   46
使用M3UA协议的接口           56
使用GTP协议的接口的信令消息  56
使用Diameter协议的接口       56
Gb接口的信令消息             56
Ga接口                       56
Iu接口的信令消息             56
DNS接口                      56
SLs接口                      56
SGs接口                      56
SBc接口                      56
S102接口                     56
Tm接口                       56
仍有后续报告输出...
---    END

%%LST IFDSCP:;%%
RETCODE = 0  执行成功。

指定信令报文的DSCP查询结果如下
--------------
消息类型  =  GTP数据报文触发的GTPU信令消息
  DSCP值  =  10
仍有后续报告输出...
---    END

%%LST IFDSCP:;%%
RETCODE = 0  执行成功。

数据报文的DSCP查询结果如下
--------------
      SNDCP转GTP数据的DSCP值  =  46
            数据DSCP使用策略  =  透传DSCP值
          会话类数据的DSCP值  =  快速转发
            流类数据的DSCP值  =  确保转发41
 交互类优先级1的数据的DSCP值  =  确保转发31
 交互类优先级2的数据的DSCP值  =  确保转发21
 交互类优先级3的数据的DSCP值  =  确保转发11
          背景类数据的DSCP值  =  尽力转发
(结果个数 = 16)
共3条报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口DSCP配置(LST-IFDSCP)_72345811.md`
