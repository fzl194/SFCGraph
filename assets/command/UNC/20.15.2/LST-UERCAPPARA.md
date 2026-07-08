---
id: UNC@20.15.2@MMLCommand@LST UERCAPPARA
type: MMLCommand
name: LST UERCAPPARA（查询UE Radio Capability信元参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UERCAPPARA
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- UE无线能力参数
status: active
---

# LST UERCAPPARA（查询UE Radio Capability信元参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查看UE无线能力的告警阈值。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UERCAPPARA]] · UE Radio Capability信元参数（UERCAPPARA）

## 使用实例

查询UE Radio Capability信元参数 “上报告警百分比” ；

LST UERCAPPARA:;

```
%%LST UERCAPPARA:;%% 
RETCODE = 0  操作成功  
查询结果如下 
------------ 
上报告警百分比  =  95 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UERCAPPARA.md`
