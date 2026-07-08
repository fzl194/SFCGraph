---
id: UDG@20.15.2@MMLCommand@LST FABRICSUBHEALTHY
type: MMLCommand
name: LST FABRICSUBHEALTHY（查询Fabric亚健康全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FABRICSUBHEALTHY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# LST FABRICSUBHEALTHY（查询Fabric亚健康全局配置）

## 功能

该命令用于查询全局亚健康相关配置：包括亚健康阈值和亚健康检测周期。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICSUBHEALTHY]] · FABRIC内联口亚健康信息（FABRICSUBHEALTHY）

## 使用实例

查询全局亚健康相关配置：

```
LST FABRICSUBHEALTHY:;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
                     亚健康阈值  =  50
            亚健康探测周期（s）  =  30
         Fabric链路切换是否使能  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Fabric亚健康全局配置（LST-FABRICSUBHEALTHY）_92520019.md`
