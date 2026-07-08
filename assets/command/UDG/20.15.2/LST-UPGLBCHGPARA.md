---
id: UDG@20.15.2@MMLCommand@LST UPGLBCHGPARA
type: MMLCommand
name: LST UPGLBCHGPARA（查询全局计费参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGLBCHGPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 用户面全局计费参数
status: active
---

# LST UPGLBCHGPARA（查询全局计费参数）

## 功能

**适用NF：PGW-U、UPF**

查询全局计费参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPGLBCHGPARA]] · 全局计费参数（UPGLBCHGPARA）

## 使用实例

查询用户面全局计费参数：

```
LST UPGLBCHGPARA:;
```

```

RETCODE = 0  操作成功. 

全局计费参数 
--------------------------------------- 
配额申请时报文动作  = 缓存
流量阈值上报最小时长间隔（500毫秒） = 2
               离线事件计费上报阈值 = 5
                       事件计费方式 = SCUR
                       计费核查开关 = 使能
                       流量备份开关 = 使能
                 流量备份阈值（MB） = 2
               流量备份间隔（分钟） = 10
      承载计费CreditPooling功能开关 = 使能
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPGLBCHGPARA.md`
