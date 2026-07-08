---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGMPLS
type: MMLCommand
name: LST AUTOSCALINGMPLS（查询MPLS自动化配置模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGMPLS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- MPLS自动化配置
status: active
---

# LST AUTOSCALINGMPLS（查询MPLS自动化配置模板）

## 功能

该命令用于查询MPLS自动化配置模板。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOSCALINGMPLS]] · MPLS自动化配置模板（AUTOSCALINGMPLS）

## 使用实例

查询MPLS自动化配置模板：

```
LST AUTOSCALINGMPLS:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
    服务名称  =  service1
最大传输单元  =  1500
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AUTOSCALINGMPLS.md`
