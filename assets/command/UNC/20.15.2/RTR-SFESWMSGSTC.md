---
id: UNC@20.15.2@MMLCommand@RTR SFESWMSGSTC
type: MMLCommand
name: RTR SFESWMSGSTC（清除FEISW消息统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: SFESWMSGSTC
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI消息统计
status: active
---

# RTR SFESWMSGSTC（清除FEISW消息统计）

## 功能

该命令用来清除FEISW消息统计。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：指定系统中有效的资源单元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFESWMSGSTC]] · FEISW消息统计（SFESWMSGSTC）

## 使用实例

清除FEISW消息统计：

```
RTR SFESWMSGSTC: RUNAME="VNRS_IPCTRL_EX_RU_0201";
RETCODE = 0  操作成功。

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除FEISW消息统计（RTR-SFESWMSGSTC）_00841409.md`
