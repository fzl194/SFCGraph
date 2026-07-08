---
id: UNC@20.15.2@MMLCommand@LST SMARTACTPARA
type: MMLCommand
name: LST SMARTACTPARA（查询激活抑制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMARTACTPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- 激活抑制参数管理
status: active
---

# LST SMARTACTPARA（查询激活抑制参数）

## 功能

**适用网元：SGSN**

此命令用于查询激活抑制相关参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMARTACTPARA]] · 激活抑制参数（SMARTACTPARA）

## 使用实例

查询激活抑制参数:

LST SMARTACTPARA:;

```
%%LST SMARTACTPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
---------------
           识别异常激活行为的门限(times/h)  =  30
                       抑制唤醒定时器(min)  =  60
                               Parking APN  =  NULL
分离异常用户的SERVICE REQUEST门限(times/h)  =  100
       分离异常用户的激活行为门限(times/h)  =  100
                特定原因值拒绝激活唤醒开关  =  关
                 Parking APN假激活唤醒开关  =  开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMARTACTPARA.md`
