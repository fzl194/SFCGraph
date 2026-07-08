---
id: UNC@20.15.2@MMLCommand@LST SDAPINTF
type: MMLCommand
name: LST SDAPINTF（查询Sdup接口参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDAPINTF
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup接口参数管理
status: active
---

# LST SDAPINTF（查询Sdup接口参数）

## 功能

**适用网元：MME**

本命令用于查询Sdup接口的管理参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDAPINTF]] · Sdup接口参数（SDAPINTF）

## 使用实例

查询Sdup接口的管理参数记录：

LST SDAPINTF:;

```
%%LST SDAPINTF:;%%
RETCODE = 0  操作成功

操作结果如下：
-------------------------
  Sdup接口侦听端口号  =  29274
 Sdup接口UDP校验功能  =  开启
    Sdup接口探测功能  =  开启
Sdup接口探测间隔时长  =  60
    Sdup链路告警阈值  =  5
    SDAP重启计数功能  =  开启
           IP地址策略 = 仅使用IPv4地址
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SDAPINTF.md`
