---
id: UDG@20.15.2@MMLCommand@DSP TRCFILEDIAG
type: MMLCommand
name: DSP TRCFILEDIAG（显示跟踪文件可维护性信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TRCFILEDIAG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 跟踪管理调测
status: active
---

# DSP TRCFILEDIAG（显示跟踪文件可维护性信息）

## 功能

该命令用于显示跟踪文件可维护性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 动作 | 可选必选说明：必选参数<br>参数含义：该参数用来指定文件流程的处理类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- generate：生成文件。<br>- export：导出文件。<br>- delete：删除文件。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [跟踪文件可维护性信息（TRCFILEDIAG）](configobject/UDG/20.15.2/TRCFILEDIAG.md)

## 使用实例

- 显示生成跟踪文件可维护性信息，可通过如下命令显示：
  ```
  DSP TRCFILEDIAG:ACTION=generate
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  编号    触发时间               跟踪任务号    跟踪文件编号    错误码

  0       2018-07-03 15:23:47    1             0               2     
  1       2018-07-03 15:24:47    1             0               2     
  (结果个数 = 2)
  ---    END
  ```
- 显示导出跟踪文件可维护性信息，可通过如下命令显示：
  ```
  DSP TRCFILEDIAG:ACTION=export
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  ----------------------
  触发时间               开始时间      结束时间    进度上报周期（秒）     指定收集文件大小上限（兆字节）    Netconf连接session     错误码 
  2016-03-19T09:23:35    NULL          NULL        10                     20                                1231                   12344      
  2016-03-19T09:24:13    NULL          NULL        10                     30                                1231                   394848     
  (结果个数 = 2)
  ---    END
  ```
- 显示删除跟踪信息收集文件可维护性信息，可通过如下命令显示：
  ```
  DSP TRCFILEDIAG:ACTION=delete
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  ----------------------
            触发时间  =  2016-03-19T09:49:20
  Netconf连接session  =  1865
            文件名称  =  home:/trace/Trace_134.zip
              错误码  =  13344
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示跟踪文件可维护性信息（DSP-TRCFILEDIAG）_59103525.md`
