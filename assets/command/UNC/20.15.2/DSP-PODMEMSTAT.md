---
id: UNC@20.15.2@MMLCommand@DSP PODMEMSTAT
type: MMLCommand
name: DSP PODMEMSTAT（查询pod内存信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PODMEMSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP PODMEMSTAT（查询pod内存信息）

## 功能

该命令用于查询所有被资源管理器管理的pod或指定pod内存信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | pod类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定pod类型。该值来自于<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>返回结果中的Pod类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的pod类型。 |
| PODID | Pod ID | 可选必选说明：可选参数<br>参数含义：本参数用于指定Pod ID。该值来自于<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>返回结果中的PODID去掉最后的IP地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的pod ID。 |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询pod的内存信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的网元ID。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PODMEMSTAT]] · pod内存信息（PODMEMSTAT）

## 使用实例

- 查询所有被资源管理器管理的Pod内存信息。
  ```
  %%DSP PODMEMSTAT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  Pod类型   Pod ID                网元ID   内存使用量(MB)     内存使用率(%)      内存总量(MB)   内存使用率历史最大值(%)  告警上报阈值(%)    告警恢复阈值(%)  

  sfm-pod   sfm-pod-mkpjm          0         306              0.67              46014            1.70                   80               70
  sfm-pod   sfm-pod-q6h5f          0         261              1.20              21822            1.90                   80               70
  sfm-pod   sfm-pod-fnnmt          0         339              1.56              21822            1.88                   80               70
  (结果个数 = 3)
  ```
- 查询进程类型为sfm-pod的所有Pod内存信息。
  ```
  %%DSP PODMEMSTAT:PODTYPE="sfm-pod";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  Pod类型   Pod ID                网元ID   内存使用量(MB)     内存使用率(%)      内存总量(MB)   内存使用率历史最大值(%)  告警上报阈值(%)  告警恢复阈值(%)

  sfm-pod   sfm-pod-mkpjm          0         306              0.67              46014            1.70                   80               70
  sfm-pod   sfm-pod-q6h5f          0         261              1.20              21822            1.90                   80               70
  sfm-pod   sfm-pod-fnnmt          0         339              1.56              21822            1.88                   80               70
  (结果个数 = 3)
  ```
- 查询Pod ID为sfm-pod-mkpjm的Pod内存信息。
  ```
  %%DSP PODMEMSTAT: PODID="sfm-pod-mkpjm";%%
  RETCODE = 0  操作成功

  结果如下
  ---------
                 Pod类型   =  sfm-pod
                  Pod ID   =  sfm-pod-mkpjm
                 网元 ID   =   0
           内存使用量(MB)  =  306
            内存使用率(%)  =  0.67
             内存总量(MB)  =  46014
  内存使用率历史最大值(%)  =  1.70
          告警上报阈值(%)  =  80
          告警恢复阈值(%)  =  70
  (结果个数 = 1)
  ```
- 查询Pod类型为sfm-pod，且Pod id为sfm-pod-mkpjm的Pod的内存信息。
  ```
  %%DSP PODMEMSTAT: PODTYPE="sfm-pod", PODID="sfm-pod-mkpjm";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                 Pod类型   =  sfm-pod
                  Pod ID   =  sfm-pod-mkpjm
                 网元 ID   =   0
           内存使用量(MB)  =  306
            内存使用率(%)  =  0.67
             内存总量(MB)  =  46014
  内存使用率历史最大值(%)  =  1.70
          告警上报阈值(%)  =  80
          告警恢复阈值(%)  =  70
   
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PODMEMSTAT.md`
