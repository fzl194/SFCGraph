---
id: UNC@20.15.2@MMLCommand@LST NGAPCMPT
type: MMLCommand
name: LST NGAPCMPT（查询NGAP兼容性参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGAPCMPT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP兼容性参数管理
status: active
---

# LST NGAPCMPT（查询NGAP兼容性参数）

## 功能

**适用NF：AMF**

该命令用于查询NGAP（NG Application Protocol）兼容性控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGAPCMPT]] · NGAP兼容性参数（NGAPCMPT）

## 使用实例

查询系统中当前配置的NGAP兼容性参数，执行如下命令：

```
%%LST NGAPCMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                           是否携带RAT限制信元  =  是
                      是否携带禁止区域信息信元  =  是
                      是否携带服务区域信息信元  =  是
                    是否携带核心网类型限制信元  =  是
                 是否携带Last E-UTRAN PLMN信元  =  是
                        是否携带感兴趣区域列表  =  是
                        感兴趣区域列表携带方式  =  全量
                    互操作原因值是否定制化映射  =  是
                         是否携带GUAMI类型信元  =  是
                     是否携带Masked IMEISV信元  =  是
是否携带Redirection for Voice EPS Fallback信元  =  是
                          是否携带扩展的UE标识  =  是
                              是否携带RFSP信元  =  是
                     Masked IMEISV信元编码方式  =  正序BIT STRING
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGAPCMPT.md`
