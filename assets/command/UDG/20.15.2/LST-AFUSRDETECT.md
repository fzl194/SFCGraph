---
id: UDG@20.15.2@MMLCommand@LST AFUSRDETECT
type: MMLCommand
name: LST AFUSRDETECT（查询计费欺诈用户检测功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AFUSRDETECT
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈用户检测功能
status: active
---

# LST AFUSRDETECT（查询计费欺诈用户检测功能）

## 功能

**适用NF：UPF**

该命令用来查询用户欺诈流量检测功能开关，及相关控制参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFUSRDETECT]] · 计费欺诈用户检测功能（AFUSRDETECT）

## 使用实例

查询用户欺诈流量检测功能配置信息：

```
LST AFUSRDETECT:;
```

```

RETCODE = 0  操作成功。

计费欺诈用户检测功能信息
------------------------
计费防欺诈用户检测功能开关  =  使能
          用户检测结果数量  =  100
              历史周期天数  =  1
              内部计算周期  =  15
              流量比例权重  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询计费欺诈用户检测功能（LST-AFUSRDETECT）_16216977.md`
