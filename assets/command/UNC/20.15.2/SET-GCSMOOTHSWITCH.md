---
id: UNC@20.15.2@MMLCommand@SET GCSMOOTHSWITCH
type: MMLCommand
name: SET GCSMOOTHSWITCH（设置GC平滑开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GCSMOOTHSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 流控管理
status: active
---

# SET GCSMOOTHSWITCH（设置GC平滑开关）

## 功能

该命令用于设置GC（Garbage Collection）平滑开关，决定流控模块计算CPU时是否需要刨除GC。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| STATUS | DURATION | TOKEN |
| --- | --- | --- |
| ON | 60 | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATUS | GC平滑开关 | 可选必选说明：必选参数<br>参数含义：该参数用于标识是否需要打开GC（Garbage Collection）平滑开关。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：<br>在需要刨除GC在CPU的影响时，需要设置STATUS为ON。 |
| DURATION | 令牌刷新周期 | 可选必选说明：可选参数<br>参数含义：该参数用于设置GC（Garbage Collection）平滑采样的周期，单位秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GCSMOOTHSWITCH查询当前参数配置值。<br>配置原则：无 |
| TOKEN | 特定周期内最大GC刨除次数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定周期内最大GC（Garbage Collection）刨除次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GCSMOOTHSWITCH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GCSMOOTHSWITCH]] · GC平滑开关（GCSMOOTHSWITCH）

## 使用实例

设置GC（Garbage Collection）平滑开关为开，且60s内最多平滑处理5次。

```

%%SET GCSMOOTHSWITCH: STATUS=ON, DURATION=60, TOKEN=5;%%
RETCODE = 0  操作成功

---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-GCSMOOTHSWITCH.md`
