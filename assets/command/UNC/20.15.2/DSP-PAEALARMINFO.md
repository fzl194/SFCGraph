---
id: UNC@20.15.2@MMLCommand@DSP PAEALARMINFO
type: MMLCommand
name: DSP PAEALARMINFO（显示PAE告警信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEALARMINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- Fabric
status: active
---

# DSP PAEALARMINFO（显示PAE告警信息）

## 功能

该命令用于显示PAE告警信息。

PAE告警信息是指本端资源的链路故障数。通过此命令可查看本端资源到所有对端资源的链路故障数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [PAE告警信息（PAEALARMINFO）](configobject/UNC/20.15.2/PAEALARMINFO.md)

## 使用实例

- 显示微服务类型为“104”微服务实例为“sfm-pod-7b4bc4fd54-6tcbb172-16-0-45__103__0”的PAE告警信息：
  ```
  %%DSP PAEALARMINFO: CELLTYPE="104", CELLINSTANCE="sfm-pod-7b4bc4fd54-6tcbb172-16-0-45__103__0";%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
    微服务类型  =  104
  微服务实例号  =  sfm-pod-7b4bc4fd54-6tcbb172-16-0-45__103__0
        平面ID  =  0
      事件名称  =  PAE_ALERT_FABRIC_PLANE_UNREACH
      端口名称  =  NA
    链接故障数  =  6
  (结果个数 = 1)

  ---    END
  ```
- 显示所有PAE告警信息：
  ```
  %%DSP PAEALARMINFO;%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
  微服务类型  微服务实例号                                平面ID  事件名称                        端口名称  链接故障数  

  104         gcp-pod-0172-16-0-83__103__0                0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         udgctrl-pod-0172-16-0-166__103__0           0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         vupctrlds-pod-0172-16-1-121__103__0         0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         vupctrld-pod-0172-16-1-112__103__0          0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         udgctrl-pod-1172-16-0-84__103__0            0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         npmu-pod-0172-16-0-251__103__0              0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         udgspu-pod-1172-16-1-113__103__0            0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         sfm-pod-5fb6fb84cd-v8lqp172-16-0-63__103__0 0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         csdb-pod-0172-16-0-247__103__0              0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         npmu-pod-1172-16-1-122__103__0              0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         sfm-pod-5fb6fb84cd-jqmnv172-16-0-15__103__0 0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         sfm-pod-5fb6fb84cd-mvvqf172-16-0-47__103__0 0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         udgspu-pod-0172-16-1-117__103__0            0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         gcp-pod-1172-16-0-165__103__0               0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  (结果个数 = 14)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE告警信息（DSP-PAEALARMINFO）_89532386.md`
