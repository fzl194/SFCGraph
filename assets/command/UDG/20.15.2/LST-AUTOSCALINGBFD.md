---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGBFD
type: MMLCommand
name: LST AUTOSCALINGBFD（查询BFD会话自动化配置模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGBFD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- BFD会话自动化配置
status: active
---

# LST AUTOSCALINGBFD（查询BFD会话自动化配置模板）

## 功能

该命令用于查询FD会话自动化配置模板。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | 模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BFD自动化配置模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～59。不支持空格和中文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOSCALINGBFD]] · BFD会话自动化配置模板（AUTOSCALINGBFD）

## 使用实例

查询BFD会话自动化配置模板：

```
LST AUTOSCALINGBFD:;
```

```

RETCODE = 0   操作成功

结果如下
------------------------
                   模板名称   =  bfdtemp
                   服务名称   =  NULL
                    BFD类型   =  Dynamic
                     IP版本   =  NULL
                   目的地址   =  ::
单臂Echo会话的收包间隔（ms）  =  NULL
 动态BFD会话的收包间隔（ms）  =  35
 动态BFD会话的发包间隔（ms）  =  35
                   检测倍数   =  7
                   单臂Echo   =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BFD会话自动化配置模板（LST-AUTOSCALINGBFD）_00841725.md`
