---
id: UNC@20.15.2@MMLCommand@LST PERFGBPAGING
type: MMLCommand
name: LST PERFGBPAGING（查询Gb接口寻呼数据）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFGBPAGING
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# LST PERFGBPAGING（查询Gb接口寻呼数据）

## 功能

**适用网元：SGSN**

该命令用于查看2G寻呼配置参数。

## 注意事项

- 不输入参数，表示查询所有参数。
- 输入参数“LAI”时，查询所有属于该LAI的参数。
- 输入参数“LAI”＋“RAC”，则查询由LAI和RAC唯一确定的参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | 寻呼范围位置区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区所在的位置区标识，与RAC共同构成路由区标识。LAI = MNC + MCC + LAC。<br>数据来源：整网规划<br>取值范围：9~10位十六进制数<br>默认值：无 |
| RAC | 寻呼范围路由区编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区在位置区内的标识，与LAI共同构成路由区标识。<br>数据来源：整网规划<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：RAC是十六进制数，占1个字节。 |
| RAITYPE | 寻呼范围路由区上报类型 | 可选必选说明：可选参数<br>参数含义：待查询的Gb模式路由区号测量对象的类型。<br>数据来源：整网规划<br>取值范围：<br>- “MANU(手动配置)”：通过[**ADD PERFGBPAGING**](增加Gb接口寻呼数据(ADD PERFGBPAGING)_26306002.md)命令创建的Gb模式路由区号对象。<br>- “AUTO(自动配置)”：系统动态上报的Gb模式路由区号对象。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFGBPAGING]] · Gb接口寻呼数据（PERFGBPAGING）

## 使用实例

查询Gb接口所有寻呼数据：

LST PERFGBPAGING:;

```
%%LST PERFGBPAGING:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
寻呼范围位置区标识    寻呼范围路由区编码    寻呼范围路由区上报类型    

123031111
             0x02                  手动配置                        

123032111
             0x01                  手动配置                 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFGBPAGING.md`
