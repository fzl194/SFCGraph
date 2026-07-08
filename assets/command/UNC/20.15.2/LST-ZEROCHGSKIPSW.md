---
id: UNC@20.15.2@MMLCommand@LST ZEROCHGSKIPSW
type: MMLCommand
name: LST ZEROCHGSKIPSW（查询零流量计费事件忽略开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ZEROCHGSKIPSW
command_category: 查询类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费参数
status: active
---

# LST ZEROCHGSKIPSW（查询零流量计费事件忽略开关）

## 功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于显示零流量计费事件忽略开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ZEROCHGSKIPSW]] · 零流量计费事件忽略开关（ZEROCHGSKIPSW）

## 使用实例

要显示零流量计费事件忽略开关：

```
LST ZEROCHGSKIPSW:;
```

```

RETCODE = 0  操作成功。

零流量计费事件忽略配置
----------------
                       零流量计费事件忽略总开关  =  ENABLE
                                    忽略RAT更新  =  DISABLE
                       忽略Serving Node地址改变  =  DISABLE
                                 忽略MS时区改变  =  DISABLE
                  忽略Serving Node PLMN标识改变  =  DISABLE
                                   忽略时间阈值  =  DISABLE
                                       忽略CCFH  =  DISABLE
                                 忽略去激活话单  =  ENABLE
        忽略PS-Furnish-Charging-Information改变  =  DISABLE
                               忽略强制生成话单  =  ENABLE
                   忽略基于位置的计费订阅和取消  =  DISABLE
                                    忽略QoS改变  =  DISABLE
                                    忽略ULI改变  =  DISABLE
                                   忽略费率切换  =  DISABLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ZEROCHGSKIPSW.md`
