---
id: UNC@20.15.2@MMLCommand@LST PCCFAILACTION
type: MMLCommand
name: LST PCCFAILACTION（查询PCC故障处理）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCFAILACTION
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
- PCC公共参数
status: active
---

# LST PCCFAILACTION（查询PCC故障处理）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询PCC故障处理动作。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCCFAILACTION]] · PCC故障处理（PCCFAILACTION）

## 使用实例

查询PCC故障处理：

```
LST PCCFAILACTION:;
```

```

RETCODE = 0  操作成功

PCC故障处理参数
---------------
                    选择PCRF/PCF失败动作  =  缺省
 选择PCRF/PCF失败回滚为Local PCC用户类型  =  回滚为本地PCC用户
选择PCRF/PCF失败回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
                 Initial流程故障处理动作  =  激活失败
  Initial流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
 Initial流程故障回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
                  Update流程故障处理动作  =  继续与PCRF/PCF交互
   Update流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
                  流量上报失败时处理动作  =  使用UPDATEFAILACT参数配置
                         SCP故障重选开关  =  SCP故障不进行重选
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCCFAILACTION.md`
