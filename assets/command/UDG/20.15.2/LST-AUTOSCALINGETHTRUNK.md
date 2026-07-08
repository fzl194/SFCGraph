---
id: UDG@20.15.2@MMLCommand@LST AUTOSCALINGETHTRUNK
type: MMLCommand
name: LST AUTOSCALINGETHTRUNK（查询以太网隧道自动化多虚拟网卡配置模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOSCALINGETHTRUNK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 以太网隧道多虚拟网卡自动化配置
status: active
---

# LST AUTOSCALINGETHTRUNK（查询以太网隧道自动化多虚拟网卡配置模板）

## 功能

该命令用于查询以太网隧道多虚拟网卡自动化配置模板信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ETHTRUNKTMPID | 以太Trunk模板ID | 可选必选说明：可选参数<br>参数含义：该参数用来指定以太Trunk模板ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～99。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AUTOSCALINGETHTRUNK]] · 以太网隧道自动化多虚拟网卡配置模板（AUTOSCALINGETHTRUNK）

## 使用实例

查询以太网隧道多虚拟网卡自动化配置模板信息：

```
LST AUTOSCALINGETHTRUNK: ETHTRUNKTMPID=1;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
以太网Trunk ID  =  1
多个虚拟网卡ID  =  3 4 5
工作模式        =  Lacp
最小激活链路数  = 1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AUTOSCALINGETHTRUNK.md`
