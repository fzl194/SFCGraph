---
id: UNC@20.15.2@MMLCommand@LST AMFUDMBYPASS
type: MMLCommand
name: LST AMFUDMBYPASS（查询AMF的UDM故障BYPASS功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFUDMBYPASS
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障BYPASS功能
status: active
---

# LST AMFUDMBYPASS（查询AMF的UDM故障BYPASS功能）

## 功能

**适用NF：AMF**

该命令用于查询AMF的UDM全故障BYPASS功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFUDMBYPASS]] · 用户UDM Bypass信息（AMFUDMBYPASS）

## 使用实例

查询AMF的UDM全故障BYPASS功能，执行如下命令：

```
%%LST AMFUDMBYPASS:;%%
RETCODE = 0  操作成功

结果如下
--------
    UDM全故障Bypass开关  =  关闭
 退出Bypass状态恢复动作  =  优雅去注册
    故障探测速率(个/秒)  =  2
       扫描时间间隔(秒)  =  60
        上报异常CHR开关  =  关闭
               部署模式  =  合设
 UDM Bypass自动退出开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFUDMBYPASS.md`
