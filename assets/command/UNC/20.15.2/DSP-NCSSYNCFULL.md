---
id: UNC@20.15.2@MMLCommand@DSP NCSSYNCFULL
type: MMLCommand
name: DSP NCSSYNCFULL（显示全量同步操作的诊断信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSSYNCFULL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSSYNCFULL（显示全量同步操作的诊断信息）

## 功能

该命令用于显示全量同步操作的诊断信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NCSSYNCFULL]] · 全量同步操作的诊断信息（NCSSYNCFULL）

## 使用实例

显示全量同步操作的诊断信息：

```
DSP NCSSYNCFULL:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
                          文件传输标识  =  0x10056
                  标志是否收到测试文件  =  TRUE
              标志测试文件是否传输结束  =  TRUE
              标志是否收到全量同步文件  =  TRUE
          标志全量同步文件是否传输结束  =  TRUE
                    全量同步文件夹名称  =  SyncFiles_1
全量同步文件名称（文件大小，单位字节）  =  cfgsynfile.zip ( 28222 )
                          文件传输进度  =  100
                              传输方法  =  Auto
                              传输协议  =  SFTP
                              操作标识  =  1
                    全量同步文件SHA1码  =  NULL
                                流控ID  =  19
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCSSYNCFULL.md`
