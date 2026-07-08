---
id: UNC@20.15.2@MMLCommand@LST IMSBYPASSFUNC
type: MMLCommand
name: LST IMSBYPASSFUNC（查询语音PCF/PCRF故障Bypass场景功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSBYPASSFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 语音PCF_PCRF Bypass管理
status: active
---

# LST IMSBYPASSFUNC（查询语音PCF/PCRF故障Bypass场景功能）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询语音PCF/PCRF故障Bypass场景功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSBYPASSFUNC]] · 语音PCF/PCRF故障Bypass场景功能（IMSBYPASSFUNC）

## 使用实例

查询语音PCF/PCRF故障Bypass场景功能：

```
%%LST IMSBYPASSFUNC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
          无语音专载时的故障非预期Bypass场景的异常处理动作  =  继承
存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作  =  继承
         存在语音专载时更新流程故障回滚为Local PCC用户类型  =  回滚PCC用户为本地PCC用户并且继续使用PCRF/PCF策略
                    非直连场景下退出Bypass发送探测消息开关  =  不发送探测消息
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询语音PCF_PCRF故障Bypass场景功能（LST-IMSBYPASSFUNC）_13938054.md`
