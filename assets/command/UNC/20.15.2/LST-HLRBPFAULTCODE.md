---
id: UNC@20.15.2@MMLCommand@LST HLRBPFAULTCODE
type: MMLCommand
name: LST HLRBPFAULTCODE（查询HLR BYPASS故障状态码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HLRBPFAULTCODE
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HLR BYPASS故障状态码
status: active
---

# LST HLRBPFAULTCODE（查询HLR BYPASS故障状态码）

## 功能

**适用网元：SGSN**

该命令用于查询配置的HLR BYPASS故障状态码信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 生效范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定特定故障码的生效范围。<br>取值范围：<br>- ALL（整系统）：整系统 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HLRBPFAULTCODE]] · HLR BYPASS故障状态码（HLRBPFAULTCODE）

## 使用实例

查询已经配置的所有HLR BYPASS故障状态码数据。

```
%%LST HLRBPFAULTCODE:;%% 
RETCODE = 0  操作成功 
The result is as follows 
------------------------ 
  生效范围  =  整系统
    故障码  =  3002
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HLRBPFAULTCODE.md`
