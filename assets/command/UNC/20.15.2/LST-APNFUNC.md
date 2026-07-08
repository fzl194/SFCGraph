---
id: UNC@20.15.2@MMLCommand@LST APNFUNC
type: MMLCommand
name: LST APNFUNC（查询APNNI功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNFUNC
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
- 会话管理
- APN功能配置
status: active
---

# LST APNFUNC（查询APNNI功能配置）

## 功能

**适用网元：SGSN**

该命令用于查询APNNI功能。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNFUNC]] · APNNI功能配置（APNFUNC）

## 使用实例

查询所有APNNI的属性信息：

**LST APNFUNC:;**

```
%%LST APNFUNC:;%% 
RETCODE = 0    执行成功。       

操作结果如下 
---------------
APN网络标识   APN用途

HUAWEI1.COM  VIP 用户
HUAWEI2.COM  VIP 用户
（结果个数 = 2）

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNFUNC.md`
