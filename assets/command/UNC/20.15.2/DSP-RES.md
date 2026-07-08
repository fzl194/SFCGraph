---
id: UNC@20.15.2@MMLCommand@DSP RES
type: MMLCommand
name: DSP RES（显示资源信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# DSP RES（显示资源信息）

## 功能

该命令用于显示资源的基本信息。用户可用该命令查看资源的名称、类型、运行状况等信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源名称，指节点或容器的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [资源信息（RES）](configobject/UNC/20.15.2/RES.md)

## 使用实例

- 显示所有资源的信息：
  ```
  DSP RES:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  逻辑资源编号    资源名称       VNFM分配的资源编号    VIM分配的资源编号                       资源实例类型    运行状态    内存容量（MB）    存储容量（GB）   CPU核数量    内存利用率（%）    CPU利用率（%）    磁盘利用率（%）    HA组    亲和性组    扩展组    主机位置                                主机名称                资源类型    父资源名称                               位置信息                          CPU架构类型
  1               OMU1           NE=34618142           92a109d2-5aef-4f64-8c13-dd625d56aeaf    OMU             正常        16384             546              4            20                 5                 20                 NULL    NULL        NULL      48645528-D21D-B211-88D4-001823E5F68B    S19_RN43_SRN0_Host20    
  容器
        
  nps-omum-node-app-66a8e66e-0
            X.X.X.X,az1.dc1,az2.dc1,HASrv1    X86
  2               OMU2           NE=34618143           634cc600-486b-484c-a033-bb6ec1729c40    OMU             正常        16384             546              4            18                 3                 20                 NULL    NULL        NULL      4246A128-D21D-B211-AC08-001823E5F68B    S19_RN43_SRN0_Host7     
  容器
        
  nps-omum-node-app-66a8e66e-0
            X.X.X.X,az1.dc1,az2.dc1,HASrv1    X86
  (结果个数 = 2)
  ---    END
  ```
- 显示名称为OMU1的资源信息：
  ```
  DSP RES:RESNAME="OMU1";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
        逻辑资源编号  =  1
            资源名称  =  OMU1
  VNFM分配的资源编号  =  NE=34618142
   VIM分配的资源编号  =  92a109d2-5aef-4f64-8c13-dd625d56aeaf
        资源实例类型  =  OMU
            运行状态  =  正常
      内存容量（MB）  =  16384
      存储容量（GB）  =  546
           CPU核数量  =  4
     内存利用率（%）  =  20
      CPU利用率（%）  =  5
     磁盘利用率（%）  =  20
                HA组  =  NULL
            亲和性组  =  NULL
              扩展组  =  NULL
            主机位置  =  48645528-D21D-B211-88D4-001823E5F68B
            主机名称  =  S19_RN43_SRN0_Host20
            资源类型  =  
  容器

          父资源名称  =  
  nps-omum-node-app-66a8e66e-0

            位置信息  =  X.X.X.X,az1.dc1,az2.dc1,HASrv1
         CPU架构类型  =  X86
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示资源信息（DSP-RES）_59036939.md`
