---
id: UNC@20.15.2@MMLCommand@LST LOCALNRI
type: MMLCommand
name: LST LOCALNRI（查询本局NRI配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALNRI
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- 本局NRI配置
status: active
---

# LST LOCALNRI（查询本局NRI配置信息）

## 功能

**适用网元：SGSN**

此命令用于查询本局NRI配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POOL区标识。<br>取值范围：0～4095<br>默认值：无 |
| NRIVBGN | NRI起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRI起始值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>取值范围：0～1023<br>默认值：无<br>说明：- NRI的取值范围在0～(2n-1)，n为本Pool的NRI长度。<br>- 若POOL表的NRI长度为10，则LOCALNRI表的NRI个数必须大于等于4， NRI起始值小于等于1020。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALNRI]] · 本局NRI配置信息（LOCALNRI）

## 使用实例

查询本局所有NRI属性信息：

LST LOCALNRI:;

```
%%LST LOCALNRI:;%%
RETCODE = 0  执行成功。

LOCALNRI表
----------
        POOL区标识  =  0
         NRI起始值  =  0
           NRI个数  =  1
           NRI状态  =  UNBLOCKED
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCALNRI.md`
