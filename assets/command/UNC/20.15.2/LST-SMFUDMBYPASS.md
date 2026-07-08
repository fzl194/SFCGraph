---
id: UNC@20.15.2@MMLCommand@LST SMFUDMBYPASS
type: MMLCommand
name: LST SMFUDMBYPASS（查询SMF的UDM全故障Bypass相关功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFUDMBYPASS
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- UDM Bypass管理
- UDM Bypass策略管理
status: active
---

# LST SMFUDMBYPASS（查询SMF的UDM全故障Bypass相关功能）

## 功能

**适用NF：SMF**

该命令用于查询SMF的UDM全故障Bypass相关功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFUDMBYPASS]] · SMF的UDM全故障Bypass相关功能（SMFUDMBYPASS）

## 使用实例

查询SMF的UDM全故障Bypass功能。

```
%%LST SMFUDMBYPASS;%%
RETCODE = 0  操作成功

结果如下
--------
SMF的UDM全故障BYPASS开关  =  打开
     故障探测速率(个/秒)  =  1
        扫描时间间隔(秒)  =  600
         上报异常CHR开关  =  打开
  自动退出BYPASS功能开关  =  打开
(结果个数 = 1)

 ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFUDMBYPASS.md`
