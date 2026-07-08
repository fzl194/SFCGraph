---
id: UNC@20.15.2@MMLCommand@LST COMBASEHEALTH
type: MMLCommand
name: LST COMBASEHEALTH（查询Base平面的亚健康检测参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: COMBASEHEALTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# LST COMBASEHEALTH（查询Base平面的亚健康检测参数）

## 功能

该命令用于查询Base平面的亚健康检测参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@COMBASEHEALTH]] · Base平面通信质量（COMBASEHEALTH）

## 使用实例

查询Base平面的亚健康检测参数：

```
%%LST COMBASEHEALTH:;%%
RETCODE = 0  操作成功

结果如下
--------
      检测周期(秒)  =  1
      统计周期(秒)  =  30
亚健康告警阈值(‰)  =  50
          使能开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-COMBASEHEALTH.md`
