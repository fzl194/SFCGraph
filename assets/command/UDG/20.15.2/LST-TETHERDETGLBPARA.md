---
id: UDG@20.15.2@MMLCommand@LST TETHERDETGLBPARA
type: MMLCommand
name: LST TETHERDETGLBPARA（查询Tethering用户终端数量检测全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TETHERDETGLBPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering用户终端数量检测全局配置
status: active
---

# LST TETHERDETGLBPARA（查询Tethering用户终端数量检测全局配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询Tethering用户终端数量检测全局配置。

## 注意事项

该命令执行后需要关闭已经创建了数据面跟踪的所有跟踪任务，重新创建新的跟踪任务才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [Tethering用户终端数量检测全局配置（TETHERDETGLBPARA）](configobject/UDG/20.15.2/TETHERDETGLBPARA.md)

## 使用实例

查询Tethering用户终端数量检测全局配置信息：

```
LST TETHERDETGLBPARA:;
```

```

RETCODE = 0  操作成功

Tethering用户终端数量检测全局配置信息
-------------------------------------
                                          UDP流的控制方式  =  TETHERING-FLOW
  PCC用户Tethering终端数量检测最大Tethering个数的选择方式  =  COMMON-POLICY
                                    Tethering节点统计方式  =  CONFIG
                                            TTL防欺诈开关  =  使能
  Tethering用户终端数量检测热点终端缓存节点的老化时间(秒)  =  300
Tethering用户终端数量检测热点终端缓存节点老化时间配置参数  =  INHERIT
                                   用户级业务带宽控制选项  =  ALL-BWM-CONTROL
          Tethering用户终端数量检测缓存节点的老化时间(秒)  =  300
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Tethering用户终端数量检测全局配置（LST-TETHERDETGLBPARA）_82837446.md`
