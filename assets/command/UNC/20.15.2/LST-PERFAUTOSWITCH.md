---
id: UNC@20.15.2@MMLCommand@LST PERFAUTOSWITCH
type: MMLCommand
name: LST PERFAUTOSWITCH（查询话统对象自动生成开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFAUTOSWITCH
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象自动生成管理
status: active
---

# LST PERFAUTOSWITCH（查询话统对象自动生成开关）

## 功能

**适用网元：SGSN、MME**

该命令用于查询性能统计对象自动生成开关。

## 注意事项

无。

## 权限

manage-ug;system-ug
G_1管理员级别命令组；G_2操作员级别命令组；G_3用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIAUTOSWITCH | TAI组对象自动生成开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置TAI组对象自动生成开关。<br>数据来源：本端规划<br>取值范围：<br>- ON(打开)：TAI组对象自动生成功能打开。<br>- OFF(关闭)：TAI组对象自动生成功能关闭。<br>系统初始设置值：OFF(关闭)<br>配置原则：如果要支持TAI组对象动态创建，无需人工干预，可以打开此功能配置。如果关闭，TAI组测量对象只能通过<br>[**ADD PERFOBJ**](../性能对象管理/增加性能对象信息(ADD PERFOBJ)_26305998.md)<br>和<br>[**ADD PERFOBJRULE**](../性能对象规则管理/增加性能对象规则(ADD PERFOBJRULE)_72225873.md)<br>命令配置；如果打开，可以同时支持自动生成和手工配置两种方式上报话统对象。 |
| GBRAIAUTOSWITCH | GB路由区对象自动生成开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置GB模式路由区对象自动生成开关。<br>数据来源：本端规划<br>取值范围：<br>- ON(打开)：GB路由区对象自动生成功能打开。<br>- OFF(关闭)：GB路由区对象自动生成功能关闭。<br>系统初始设置值：OFF(关闭)<br>配置原则：如果要支持Gb模式路由区号对象动态创建，无需人工干预，可以打开此功能配置。如果关闭，此测量对象只能通过<br>[**ADD PERFGBPAGING**](../性能对象管理/增加Gb接口寻呼数据(ADD PERFGBPAGING)_26306002.md)<br>命令配置；如果打开，可以同时支持自动生成和手工配置两种方式上报话统对象。 |
| APNAUTOSWITCH | APN对象自动生成开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置APN对象自动生成开关。<br>数据来源：本端规划<br>取值范围：<br>- ON(打开)：APN对象自动生成功能打开。<br>- OFF(关闭)：APN对象自动生成功能关闭。<br>系统初始设置值：OFF(关闭)配置原则：如果要支持APN对象动态创建，无需人工干预，可以打开此功能配置。如果关闭，此测量对象只能通过<br>[**ADD PERFOBJ**](../性能对象管理/增加性能对象信息(ADD PERFOBJ)_26305998.md)<br>命令配置；如果打开，可以同时支持自动生成和手工配置两种方式上报话统对象。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFAUTOSWITCH]] · 话统对象自动生成开关（PERFAUTOSWITCH）

## 使用实例

查询话统对象自动生成开关:

LST PERFAUTOSWITCH:;

```
%%LST PERFAUTOSWITCH:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
    TAI组对象自动生成开关  =  打开
 GB路由区对象自动生成开关  =  打开
      APN对象自动生成开关  =  打开
---  END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话统对象自动生成开关(LST-PERFAUTOSWITCH)_72345793.md`
