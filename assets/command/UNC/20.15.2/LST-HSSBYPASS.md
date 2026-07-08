---
id: UNC@20.15.2@MMLCommand@LST HSSBYPASS
type: MMLCommand
name: LST HSSBYPASS（查询HSS故障Bypass功能控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSSBYPASS
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS故障BYPASS功能
status: active
---

# LST HSSBYPASS（查询HSS故障Bypass功能控制参数）

## 功能

**适用网元：MME**

该命令用于查询HSS故障Bypass功能控制参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSSBYPASS]] · HSS故障Bypass功能控制参数（HSSBYPASS）

## 使用实例

查询HSS故障Bypass功能控制参数信息：

```
LST HSSBYPASS:;
```

```
查询结果如下
-------------------------
    HSS Bypass功能开关  =  关闭
        MSISDN检查开关  =  是
退出Bypass状态恢复动作  =  补充缺失流程
 整系统扫描速率(个/秒)  =  0
      扫描时间间隔(秒)  =  600
       上报异常CHR开关  =  开启
HSS Bypass自动退出开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HSSBYPASS.md`
