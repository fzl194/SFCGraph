---
id: UDG@20.15.2@MMLCommand@LST OMNWCONF
type: MMLCommand
name: LST OMNWCONF（查询OM网络探测参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OMNWCONF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 网络管理
status: active
---

# LST OMNWCONF（查询OM网络探测参数）

## 功能

用于查询OM网络故障探测参数。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OMNWCONF]] · OM网络探测参数（OMNWCONF）

## 使用实例

查询OM网络探测参数：

```
%%LST OMNWCONF:;%% 
RETCODE = 0  操作成功  
网络探测配置如下 
---------------- 
IP类型      IP地址类型  探测周期（秒）  倒换阈值  告警阈值  网络探测开关  网络亚健康告警阈值（%）  网络亚健康检测周期（分钟）  
PHYSICALIP  IPV4        15              NULL      15        ON            10                       5
PHYSICALIP  IPV6        10              NULL      15        ON            10                       5
VIRTUALIP   IPV6        2               3         NULL      ON            NULL                     NULL
(结果个数 = 3)  
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OMNWCONF.md`
