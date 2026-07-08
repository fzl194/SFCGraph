---
id: UNC@20.15.2@MMLCommand@LST SMSFUDMBYPASS
type: MMLCommand
name: LST SMSFUDMBYPASS（查询SMSF的UDM全故障Bypass功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFUDMBYPASS
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM Bypass管理
status: active
---

# LST SMSFUDMBYPASS（查询SMSF的UDM全故障Bypass功能开关）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF的UDM全故障Bypass功能开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFUDMBYPASS]] · SMSF的UDM全故障Bypass功能开关（SMSFUDMBYPASS）

## 使用实例

运营商希望查询SMSF的UDM全故障Bypass功能开关，执行如下命令：

```
LST SMSFUDMBYPASS:;
%%LST SMSFUDMBYPASS:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
UDM全故障Bypass开关 = 打开
退出Bypass状态恢复动作 = 补充缺失的UDM流程
故障探测速率(个/秒) = 5
扫描时间间隔(秒) = 20
上报异常CHR开关 = 打开

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF的UDM全故障Bypass功能开关（LST-SMSFUDMBYPASS）_05054701.md`
