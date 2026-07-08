---
id: UNC@20.15.2@MMLCommand@SET SCALINGCFG
type: MMLCommand
name: SET SCALINGCFG（设置自动扩缩容配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCALINGCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 弹性开关
status: active
---

# SET SCALINGCFG（设置自动扩缩容配置）

## 功能

此命令用于设置扩缩容的各项参数，扩缩容方式、以及扩缩容步长、设置扩缩容阈值上下限，超过阈值上限，进行扩容，低于阈值下限进行缩容。扩缩容触发方式依赖 [**SET SCALINGSWITCH**](设置扩缩容开关（SET SCALINGSWITCH）_09587379.md) 命令。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCALEOUTTHD | SCALEINTHD | STEPCLASS | SCALINGSTEP |
| --- | --- | --- | --- |
| 80 | 20 | Percentage | 50 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCALEOUTTHD | 扩容阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扩容阈值，CPU超过该阈值触发自动扩容。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：80。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCALINGCFG查询当前参数配置值。<br>配置原则：无 |
| SCALEINTHD | 缩容阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示缩容阈值，CPU低于该阈值则触发自动缩容。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：20。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCALINGCFG查询当前参数配置值。<br>配置原则：无 |
| STEPCLASS | 扩缩容步进方式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扩缩容步进方式，可以按照数量百分比弹性，也可以扩缩容指定个数。<br>数据来源：本端规划<br>取值范围：<br>- Percentage（百分比）<br>- PodNumber（Pod数量）<br>默认值：Percentage。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCALINGCFG查询当前参数配置值。<br>配置原则：无 |
| SCALINGSTEP | 扩缩容步长 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扩缩容步长，该参数取值依赖扩缩容步进方式，代表百分比值或者个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647。<br>默认值：50。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SCALINGCFG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCALINGCFG]] · 自动扩缩容配置（SCALINGCFG）

## 使用实例

- 设置按照百分比方式弹性，步长为50%，负载阈值上限为80%，下限为20%：
  ```
  %%SET SCALINGCFG: SCALEOUTTHD=80, SCALEINTHD=20, STEPCLASS=Percentage, SCALINGSTEP=50;
  ```
- 设置按照Pod数量方式弹性，步长为2个Pod，负载阈值上限为80%，下限为20%：
  ```
  SET SCALINGCFG: SCALEOUTTHD=80, SCALEINTHD=20, STEPCLASS=PodNumber, SCALINGSTEP=2;%%
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SCALINGCFG.md`
