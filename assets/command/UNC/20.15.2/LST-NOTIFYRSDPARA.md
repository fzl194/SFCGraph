---
id: UNC@20.15.2@MMLCommand@LST NOTIFYRSDPARA
type: MMLCommand
name: LST NOTIFYRSDPARA（查询状态通知失败重传参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NOTIFYRSDPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知失败重传开关
status: active
---

# LST NOTIFYRSDPARA（查询状态通知失败重传参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF状态通知失败时重传的参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [状态通知失败重传参数（NOTIFYRSDPARA）](configobject/UNC/20.15.2/NOTIFYRSDPARA.md)

## 使用实例

查询状态通知失败重传参数：

```
LST NOTIFYRSDPARA:;
%%LST NOTIFYRSDPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
           失败通知重传开关  =  打开
 失败通知重传周期时长(分钟)  =  20
       失败通知重传最大次数  =  0
         失败通知重传状态码  =  429.500.503.504
   失败通知重传消息队列长度  =  1024
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询状态通知失败重传参数（LST-NOTIFYRSDPARA）_25121190.md`
