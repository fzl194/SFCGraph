---
id: UNC@20.15.2@MMLCommand@SET NGNTNFUNC
type: MMLCommand
name: SET NGNTNFUNC（设置卫星网络接入管理功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGNTNFUNC
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 卫星网络接入管理
status: active
---

# SET NGNTNFUNC（设置卫星网络接入管理功能）

## 功能

**适用NF：AMF**

此命令用于设置卫星网络接入管理功能。

5G NTN技术可实现手机通过卫星直接连接到蜂窝宽带网络，从而构建连接泛在、场景丰富、产业链高度融合、建设运维成本低的天地融合网络。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NTNTPACCSW |
| --- |
| NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NTNTPACCSW | NTN透明模式接入开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF是否支持透明模式的卫星接入。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGNTNFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGNTNFUNC]] · 卫星网络接入管理功能（NGNTNFUNC）

## 使用实例

设置AMF支持透明模式的卫星网络接入，执行如下命令：

```
SET NGNTNFUNC:NTNTPACCSW=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NGNTNFUNC.md`
