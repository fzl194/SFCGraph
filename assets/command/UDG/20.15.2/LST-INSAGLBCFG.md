---
id: UDG@20.15.2@MMLCommand@LST INSAGLBCFG
type: MMLCommand
name: LST INSAGLBCFG（查询智能识别全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: INSAGLBCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 智能识别全局配置
status: active
---

# LST INSAGLBCFG（查询智能识别全局配置）

## 功能

**适用NF：PGW-U、UPF**

查询智能识别全局配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/INSAGLBCFG]] · 智能识别全局配置（INSAGLBCFG）

## 使用实例

查询智能识别全局配置：

```
LST INSAGLBCFG:;
```

```

RETCODE = 0 操作成功。
 
智能识别全局配置信息
-------
             智能识别推理能力开关 = Enable
                  可信IP过滤开关 = Enable
      智能识别结果用于策略匹配开关 = Enable
         智能识别抽样比率(万分比) = 10000
             智能识别阈值(千分比) = 600
       智能识别推理超时时间(毫秒) = 200
 
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询智能识别全局配置（LST-INSAGLBCFG）_56165566.md`
